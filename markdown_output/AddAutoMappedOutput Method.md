Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AddAutoMappedOutput Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectChildSpecificationProjectDef Class](topic4067.md) : AddAutoMappedOutput Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_columnName_
    The name of the column to bind.

Glossary Item Box

Adds a new output binding to this project definition. The binding will attempt to auto map to a specification property with the same name as the column to bind. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function AddAutoMappedOutput( _
       ByVal _columnName_ As String _
    ) As [ProjectChildSpecificationOutputDef](topic4056.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectChildSpecificationProjectDef](topic4067.md)
    Dim columnName As String
    Dim value As [ProjectChildSpecificationOutputDef](topic4056.md)
     
    value = instance.AddAutoMappedOutput(columnName)  
  
C#|   
---|---  
      
    
    public [ProjectChildSpecificationOutputDef](topic4056.md) AddAutoMappedOutput( 
       string _columnName_
    )  
  
#### Parameters

 _columnName_
    The name of the column to bind.

#### Return Value

The child specification output.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectChildSpecificationProjectDef Class](topic4067.md)   
[ProjectChildSpecificationProjectDef Members](topic4068.md)


