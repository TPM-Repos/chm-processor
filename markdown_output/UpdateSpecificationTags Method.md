UpdateSpecificationTags Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSpecifications Class](topic3355.md) : UpdateSpecificationTags Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_specificationId_
    The Id of the specification to update.

_newTags_
    The new tags to associate with the specification.

Glossary Item Box

Updates the tags for the specified specification. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function UpdateSpecificationTags( _
       ByVal _specificationId_ As Integer, _
       ByVal _newTags_() As String _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupSpecifications](topic3355.md)
    Dim specificationId As Integer
    Dim newTags() As String
    Dim value As Boolean
     
    value = instance.UpdateSpecificationTags(specificationId, newTags)  
  
C#|   
---|---  
      
    
    public bool UpdateSpecificationTags( 
       int _specificationId_ ,
       string[] _newTags_
    )  
  
#### Parameters

 _specificationId_
    The Id of the specification to update.
_newTags_
    The new tags to associate with the specification.

#### Return Value

True if the tags were successfully updated, otherwise False.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupSpecifications Class](topic3355.md)   
[GroupSpecifications Members](topic3356.md)


