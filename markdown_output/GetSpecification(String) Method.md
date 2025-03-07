Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetSpecification(String) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSpecifications Class](topic3355.md) > [GetSpecification Method](topic3369.md) : GetSpecification(String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name associated with the specification to retrieve.

Glossary Item Box

Gets details about a specification with the specified name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function GetSpecification( _
       ByVal _name_ As String _
    ) As [SpecificationDetails](topic11292.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupSpecifications](topic3355.md)
    Dim name As String
    Dim value As [SpecificationDetails](topic11292.md)
     
    value = instance.GetSpecification(name)  
  
C#|   
---|---  
      
    
    public [SpecificationDetails](topic11292.md) GetSpecification( 
       string _name_
    )  
  
#### Parameters

 _name_
    The name associated with the specification to retrieve.

#### Return Value

The specification details.

# Exceptions

Exception| Description  
---|---  
[ItemNotFoundException](topic3571.md)| No specification with the given name could be found.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupSpecifications Class](topic3355.md)   
[GroupSpecifications Members](topic3356.md)   
[Overload List](topic3369.md)


