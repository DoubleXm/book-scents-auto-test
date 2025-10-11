import subprocess
import argparse
from datetime import datetime
from utils.config import config


class TestRunner:

    def __init__(self):
        self.parser = self._setup_parser()

    def _setup_parser(self):
        parser = argparse.ArgumentParser(description="书香自动化测试")

        parser.add_argument(
            "--env", choices=["dev", "production"], default="dev", help="指定测试环境"
        )
        parser.add_argument(
            "--api-test",
            help="执行 API 测试",
            action="store_const",
            const="src/api/tests",
        )
        parser.add_argument(
            "--ui-test", help="执行 UI 测试", action="store_const", const="src/ui/tests"
        )
        parser.add_argument(
            "--all-test", help="执行所有测试", action="store_const", const="src"
        )
        parser.add_argument(
            "--debug", help="开启 UI 调试模式", action="store_const", const="PWDEBUG=1"
        )
        return parser

    def _message_record(self, args, command):
        print(f"\n🚀 执行命令: {' '.join(command.split())}\n🍎 当前环境: {config.ENV}")
        if args.ui_test or args.all_test:
            print(
                f"🌐 浏览器: {config.UI_BROWSER}, 无头模式: {config.UI_HEADLESS}, UI地址: {config.UI_URL}"
            )

        if args.api_test or args.all_test:
            print(
                f"💻 API地址: {config.BASE_URL}, API超时: {config.API_TIMEOUT}, 数据库: {config.MYSQL_DATABASE}"
            )

    def build_command(self, args):
        log_file_name = f"./artifacts/logs/{config.ENV}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        command = f"{args.debug or ''} pytest {args.api_test or ''} {args.ui_test or ''} {args.all_test or ''} --log-file={log_file_name}"

        self._message_record(args, command)
        return command

    def run(self):
        args = self.parser.parse_args()
        command = self.build_command(args)
        subprocess.run(command, shell=True, check=True)


if __name__ == "__main__":
    test_runner = TestRunner()
    test_runner.run()
