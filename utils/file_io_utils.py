import requests as req
import io


def get_remote_stream(
        url:str,
        ret_mime:bool=False,
    ) -> io.BytesIO:
    resp = req.get(url, stream=True)
    resp.raise_for_status()
    rets = [io.BytesIO(resp.content)]
    if ret_mime: rets.append(resp.headers.get("Content-Type", "unknown"))
    return tuple(rets)


def get_remote_contents(
        url:str,
        codec:str="utf8",
    ) -> str:
    resp = req.get(url, stream=True)
    resp.raise_for_status()
    return resp.content.decode(codec)


if __name__ == "__main__":
    
    # ios = get_remote_stream("https://github.com/browser-use/browser-use/pull/845.diff")
    ios:bytes = get_remote_contents("https://github.com/browser-use/browser-use/pull/845.diff")
    # print(ios.decode("utf8"))
    print(ios)
    
    # while True:
    #     c = ios.read()
    #     if not c: break
    #     print(c)

