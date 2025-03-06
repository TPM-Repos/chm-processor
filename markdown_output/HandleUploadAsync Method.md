![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
HandleUploadAsync Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [UploadControl Class](topic9323.md) : HandleUploadAsync Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_inputStream_
    The stream to read the file information from.

_uploadingFileName_
    The name of the file as specified by the client.

Glossary Item Box

Takes the specified inputs and completes the upload process for this control asynchronously. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <AsyncStateMachineAttribute(DriveWorks.Forms.UploadControl+VB$StateMachine_52_HandleUploadAsync)>
    Public Function HandleUploadAsync( _
       ByVal _inputStream_ As Stream, _
       ByVal _uploadingFileName_ As String _
    ) As Task  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [UploadControl](topic9323.md)
    Dim inputStream As Stream
    Dim uploadingFileName As String
    Dim value As Task
     
    value = instance.HandleUploadAsync(inputStream, uploadingFileName)  
  
C#|   
---|---  
      
    
    [AsyncStateMachineAttribute(DriveWorks.Forms.UploadControl+VB$StateMachine_52_HandleUploadAsync)]
    public Task HandleUploadAsync( 
       Stream _inputStream_ ,
       string _uploadingFileName_
    )  
  
#### Parameters

 _inputStream_
    The stream to read the file information from.
_uploadingFileName_
    The name of the file as specified by the client.

#### Return Value

Task that will complete when the process is complete.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[UploadControl Class](topic9323.md)   
[UploadControl Members](topic9324.md)


