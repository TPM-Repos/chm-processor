TryDeleteEmbeddedSpecificationDependencies Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSpecifications Class](topic3355.md) : TryDeleteEmbeddedSpecificationDependencies Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_specificationId_
    The unique numerical identifier of the specification to remove dependencies for.

Glossary Item Box

Removes the component dependencies from the group, for the given embedded specification. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TryDeleteEmbeddedSpecificationDependencies( _
       ByVal _specificationId_ As Integer _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupSpecifications](topic3355.md)
    Dim specificationId As Integer
    Dim value As Boolean
     
    value = instance.TryDeleteEmbeddedSpecificationDependencies(specificationId)  
  
C#|   
---|---  
      
    
    public bool TryDeleteEmbeddedSpecificationDependencies( 
       int _specificationId_
    )  
  
#### Parameters

 _specificationId_
    The unique numerical identifier of the specification to remove dependencies for.

#### Return Value

True if the specification had dependencies and they were removed, false if there were no dependencies to remove.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupSpecifications Class](topic3355.md)   
[GroupSpecifications Members](topic3356.md)


