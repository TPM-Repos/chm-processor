![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Add Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic14145.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [CapturedCustomPropertyCollection Class](topic14139.md) : Add Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the custom property.

Glossary Item Box

Adds and returns a new custom property with the given name. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Add( _
       ByVal _name_ As String _
    ) As [CapturedCustomProperty](topic14132.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [CapturedCustomPropertyCollection](topic14139.md)
    Dim name As String
    Dim value As [CapturedCustomProperty](topic14132.md)
     
    value = instance.Add(name)  
  
C#|   
---|---  
      
    
    public [CapturedCustomProperty](topic14132.md) Add( 
       string _name_
    )  
  
#### Parameters

 _name_
    The name of the custom property.

#### Return Value

The newly added custom property.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[CapturedCustomPropertyCollection Class](topic14139.md)   
[CapturedCustomPropertyCollection Members](topic14140.md)

©2024 DriveWorks Ltd. All Rights Reserved.
