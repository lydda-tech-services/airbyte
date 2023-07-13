#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from source_snapchat_story_studio import SourceSnapchatStoryStudio

if __name__ == "__main__":
    source = SourceSnapchatStoryStudio()
    launch(source, sys.argv[1:])
