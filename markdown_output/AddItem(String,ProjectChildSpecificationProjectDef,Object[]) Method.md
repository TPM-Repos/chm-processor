![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AddItem(String,ProjectChildSpecificationProjectDef,Object[]) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic4026.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectChildSpecificationDef Class](topic4019.md) : AddItem(String,ProjectChildSpecificationProjectDef,Object[]) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_specificationName_
    The name of the specification to add.

_projectDef_
    The type of item to create.

_values_
    The values to set for this item.

Glossary Item Box

Adds a new item to this item list. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub AddItem( _
       ByVal _specificationName_ As String, _
       ByVal _projectDef_ As [ProjectChildSpecificationProjectDef](topic4067.md), _
       ByVal _values_() As Object _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectChildSpecificationDef](topic4019.md)
    Dim specificationName As String
    Dim projectDef As [ProjectChildSpecificationProjectDef](topic4067.md)
    Dim values() As Object
     
    instance.AddItem(specificationName, projectDef, values)  
  
C#|   
---|---  
      
    
    public void AddItem( 
       string _specificationName_ ,
       [ProjectChildSpecificationProjectDef](topic4067.md) _projectDef_ ,
       object[] _values_
    )  
  
#### Parameters

 _specificationName_
    The name of the specification to add.
_projectDef_
    The type of item to create.
_values_
    The values to set for this item.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectChildSpecificationDef Class](topic4019.md)   
[ProjectChildSpecificationDef Members](topic4020.md)

©2024 DriveWorks Ltd. All Rights Reserved.
