![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ControlDynamicPropertyRule Constructor   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic7794.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [ControlDynamicPropertyRule Class](topic7788.md) : ControlDynamicPropertyRule Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_control_
    The control that the dynamic property belongs to.

_prop_
    The dynamic property.

Glossary Item Box

Creates a new instance of the [ControlDynamicPropertyRule](topic7788.md) class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _control_ As [ControlBase](topic7698.md), _
       ByVal _prop_ As [DynamicProperty](topic9398.md) _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim control As [ControlBase](topic7698.md)
    Dim prop As [DynamicProperty](topic9398.md)
     
    Dim instance As New [ControlDynamicPropertyRule](topic7788.md)(control, prop)  
  
C#|   
---|---  
      
    
    public ControlDynamicPropertyRule( 
       [ControlBase](topic7698.md) _control_ ,
       [DynamicProperty](topic9398.md) _prop_
    )  
  
#### Parameters

 _control_
    The control that the dynamic property belongs to.
_prop_
    The dynamic property.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ControlDynamicPropertyRule Class](topic7788.md)   
[ControlDynamicPropertyRule Members](topic7789.md)

©2024 DriveWorks Ltd. All Rights Reserved.
