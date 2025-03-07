Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetSpecification(Int32) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSpecifications Class](topic3355.md) > [GetSpecification Method](topic3369.md) : GetSpecification(Int32) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_id_
    The unique numerical identifier associated with the specification to retrieve.

Glossary Item Box

Gets details about a specification with the specified identifier. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function GetSpecification( _
       ByVal _id_ As Integer _
    ) As [SpecificationDetails](topic11292.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupSpecifications](topic3355.md)
    Dim id As Integer
    Dim value As [SpecificationDetails](topic11292.md)
     
    value = instance.GetSpecification(id)  
  
C#|   
---|---  
      
    
    public [SpecificationDetails](topic11292.md) GetSpecification( 
       int _id_
    )  
  
#### Parameters

 _id_
    The unique numerical identifier associated with the specification to retrieve.

#### Return Value

The specification details.

# Exceptions

Exception| Description  
---|---  
[ItemNotFoundException](topic3571.md)| No specification with the given identifier could be found.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupSpecifications Class](topic3355.md)   
[GroupSpecifications Members](topic3356.md)   
[Overload List](topic3369.md)


