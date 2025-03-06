![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
MessageEventArgs Constructor(ProjectMessage)   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3711.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [MessageEventArgs Class](topic3704.md) > [MessageEventArgs Constructor](topic3710.md) : MessageEventArgs Constructor(ProjectMessage)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_message_
    The message that was changed.

Glossary Item Box

Initializes a new instance of the [MessageEventArgs](topic3704.md) type. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _message_ As [ProjectMessage](topic4601.md) _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim message As [ProjectMessage](topic4601.md)
     
    Dim instance As New [MessageEventArgs](topic3704.md)(message)  
  
C#|   
---|---  
      
    
    public MessageEventArgs( 
       [ProjectMessage](topic4601.md) _message_
    )  
  
#### Parameters

 _message_
    The message that was changed.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[MessageEventArgs Class](topic3704.md)   
[MessageEventArgs Members](topic3705.md)   
[Overload List](topic3710.md)

©2024 DriveWorks Ltd. All Rights Reserved.
