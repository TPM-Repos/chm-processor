Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AddItem(String,ProjectChildSpecificationProjectDef,Object[]) Method   
  
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

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub AddItem( _
       ByVal _specificationName_ As String, _
       ByVal _projectDef_ As [ProjectChildSpecificationProjectDef](topic4067.md), _
       ByVal _values_() As Object _
    )   
  
Visual Basic (Usage)| Copy Code  
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

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectChildSpecificationDef Class](topic4019.md)   
[ProjectChildSpecificationDef Members](topic4020.md)


