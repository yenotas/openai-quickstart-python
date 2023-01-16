          // var element = document.getElementById("result");
          // const
          // image = await fetch(element.getAttribute("src")),
          // blob = await image.blob();
          // await navigator.clipboard.write([
          //   new ClipboardItem({ [blob.type]: blob })
          // ]);
          // window.getSelection().removeAllRanges();
          // let range = document.createRange();
          // range.selectNode(element);
          // window.getSelection().addRange(range);
          // document.execCommand('copy');
          // window.getSelection().removeAllRanges();

          var img = document.getElementById("result");
          var canvas = document.createElement('canvas');
          canvas.width = img.clientWidth;
          canvas.height = img.clientHeight;
          var ctx = canvas.getContext('2d');
          ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
          var dataURI = canvas.toDataURL('image/png');
          console.log(dataURI)
          var blob = dataURLtoBlob(dataURI);

          navigator.clipboard.write([
            new ClipboardItem({ [blob.type]: blob })
          ]);