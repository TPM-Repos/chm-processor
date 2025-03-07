Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetChildSpecificationDetails Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectChildSpecificationDef Class](topic4019.md) : GetChildSpecificationDetails Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_specificationName_
    The name of the specification to get the details of.

Glossary Item Box

Gets the specification details for the specification name provided. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetChildSpecificationDetails( _
       ByVal _specificationName_ As String _
    ) As [SpecificationDetails](topic11292.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectChildSpecificationDef](topic4019.md)
    Dim specificationName As String
    Dim value As [SpecificationDetails](topic11292.md)
     
    value = instance.GetChildSpecificationDetails(specificationName)  
  
C#|   
---|---  
      
    
    public [SpecificationDetails](topic11292.md) GetChildSpecificationDetails( 
       string _specificationName_
    )  
  
#### Parameters

 _specificationName_
    The name of the specification to get the details of.

#### Return Value

The found specification Details or a null if not found.

# Remarks

This is the only way to get specification details for embedded specifications.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectChildSpecificationDef Class](topic4019.md)   
[ProjectChildSpecificationDef Members](topic4020.md)


