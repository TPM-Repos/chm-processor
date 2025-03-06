![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SetTopicName Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic852.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [HelpProvider Class](topic844.md) : SetTopicName Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_control_
    Control to set the topic name on.

_value_
    The help topic name to set on the control.

Glossary Item Box

Sets the help topic name for the specified control. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Sub SetTopicName( _
       ByVal _control_ As DependencyObject, _
       ByVal _value_ As String _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim control As DependencyObject
    Dim value As String
     
    [HelpProvider](topic844.md).SetTopicName(control, value)  
  
C#|   
---|---  
      
    
    public static void SetTopicName( 
       DependencyObject _control_ ,
       string _value_
    )  
  
#### Parameters

 _control_
    Control to set the topic name on.
_value_
    The help topic name to set on the control.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[HelpProvider Class](topic844.md)   
[HelpProvider Members](topic845.md)

©2024 DriveWorks Ltd. All Rights Reserved.
