![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetTopicName Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic851.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [HelpProvider Class](topic844.md) : GetTopicName Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_control_
    The control to find the topic name on.

Glossary Item Box

Gets the topic name specified in the control or on the first visual parent of the control. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function GetTopicName( _
       ByVal _control_ As DependencyObject _
    ) As String  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim control As DependencyObject
    Dim value As String
     
    value = [HelpProvider](topic844.md).GetTopicName(control)  
  
C#|   
---|---  
      
    
    public static string GetTopicName( 
       DependencyObject _control_
    )  
  
#### Parameters

 _control_
    The control to find the topic name on.

#### Return Value

Topic name specified in the given control or one of its parents.

# ![](dotnetimages/collapse.gif)Remarks

Returns nothing if no Topic name is specified in the visual tree.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[HelpProvider Class](topic844.md)   
[HelpProvider Members](topic845.md)

©2024 DriveWorks Ltd. All Rights Reserved.
