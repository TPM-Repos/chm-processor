Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Exists Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSpecifications Class](topic3355.md) : Exists Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_specificationName_
    The name of the specification to seach for.

Glossary Item Box

Determines whether a specification with the specified name already exists. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Exists( _
       ByVal _specificationName_ As String _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupSpecifications](topic3355.md)
    Dim specificationName As String
    Dim value As Boolean
     
    value = instance.Exists(specificationName)  
  
C#|   
---|---  
      
    
    public bool Exists( 
       string _specificationName_
    )  
  
#### Parameters

 _specificationName_
    The name of the specification to seach for.

#### Return Value

True if the given specification name is already registered, otherwise false.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupSpecifications Class](topic3355.md)   
[GroupSpecifications Members](topic3356.md)


