![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreatePreviewFromServerAsync Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic8718.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [PreviewControl Class](topic8709.md) : CreatePreviewFromServerAsync Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Creates a preview from the server asynchronously. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <AsyncStateMachineAttribute(DriveWorks.Forms.PreviewControl+VB$StateMachine_231_CreatePreviewFromServerAsync)>
    Public Function CreatePreviewFromServerAsync() As Task(Of PreviewServerResult)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [PreviewControl](topic8709.md)
    Dim value As Task(Of PreviewServerResult)
     
    value = instance.CreatePreviewFromServerAsync()  
  
C#|   
---|---  
      
    
    [AsyncStateMachineAttribute(DriveWorks.Forms.PreviewControl+VB$StateMachine_231_CreatePreviewFromServerAsync)]
    public Task<PreviewServerResult> CreatePreviewFromServerAsync()  
  
#### Return Value

A task that can be awaited in order to get information from the server as to the status of the preview.

# ![](dotnetimages/collapse.gif)Remarks

Previewing asynchronously will allow for multiple previews over the group connection. Note: Only one preview can be active per preview control.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[PreviewControl Class](topic8709.md)   
[PreviewControl Members](topic8710.md)

©2024 DriveWorks Ltd. All Rights Reserved.
