![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
OnCheckingFileExists Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic1665.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [IAutopilotService Interface](topic1654.md) : OnCheckingFileExists Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sender_
    The event sender.

_filePath_
    The file path to include with the event.

Glossary Item Box

Raises the [CheckingFileExists](topic1681.md) event with the provided file path. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub OnCheckingFileExists( _
       ByVal _sender_ As Object, _
       ByVal _filePath_ As String _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IAutopilotService](topic1654.md)
    Dim sender As Object
    Dim filePath As String
     
    instance.OnCheckingFileExists(sender, filePath)  
  
C#|   
---|---  
      
    
    void OnCheckingFileExists( 
       object _sender_ ,
       string _filePath_
    )  
  
#### Parameters

 _sender_
    The event sender.
_filePath_
    The file path to include with the event.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IAutopilotService Interface](topic1654.md)   
[IAutopilotService Members](topic1655.md)

©2024 DriveWorks Ltd. All Rights Reserved.
