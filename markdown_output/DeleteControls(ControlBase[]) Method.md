![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DeleteControls(ControlBase[]) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic8094.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [Form Class](topic8086.md) > [DeleteControls Method](topic8092.md) : DeleteControls(ControlBase[]) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_controls_
    The controls to delete.

Glossary Item Box

Deletes the specified controls from the form. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function DeleteControls( _
       ByVal _controls_() As [ControlBase](topic7698.md) _
    ) As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [Form](topic8086.md)
    Dim controls() As [ControlBase](topic7698.md)
    Dim value As Boolean
     
    value = instance.DeleteControls(controls)  
  
C#|   
---|---  
      
    
    public bool DeleteControls( 
       [ControlBase](topic7698.md)[] _controls_
    )  
  
#### Parameters

 _controls_
    The controls to delete.

#### Return Value

True if the controls were found and deleted.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[Form Class](topic8086.md)   
[Form Members](topic8087.md)   
[Overload List](topic8092.md)

©2024 DriveWorks Ltd. All Rights Reserved.
