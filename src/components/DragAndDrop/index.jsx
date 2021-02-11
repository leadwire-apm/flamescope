import React from "react";
import "react-dropzone-uploader/dist/styles.css";
import Dropzone from "react-dropzone-uploader";
function DragAndDrop() {
    
  const getUploadParams = ({ meta }) => {
    const url = '/upload/'
    return { url, meta: { fileUrl: `${url}/${encodeURIComponent(meta.name)}` } }
  }

  const handleChangeStatus = ({remove }, status) => {
    if (status === 'headers_received') {
      remove();
      window.location.reload(false);
    }
  }



  return (
    <Dropzone
    getUploadParams={getUploadParams}
    onChangeStatus={handleChangeStatus}
    maxFiles={1}
    multiple={false}
    canCancel={false}
    styles={{
      dropzone: { width: 400, height: 200, overflow: 'hidden' },
      dropzoneActive: { borderColor: 'green' },
    }}
  />
  );
}

export default DragAndDrop;
