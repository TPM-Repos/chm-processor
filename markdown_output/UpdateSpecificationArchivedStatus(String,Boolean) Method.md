       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
UpdateSpecificationArchivedStatus(String,Boolean) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3409.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSpecifications Class](topic3355.md) > [UpdateSpecificationArchivedStatus Method](topic3408.md) : UpdateSpecificationArchivedStatus(String,Boolean) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_specificationName_
    The name of the specification to update.

_isArchived_
    The new value of the archived flag.

Glossary Item Box

Archives or unarchives a specification. The specification must exist, and must not be running. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Sub UpdateSpecificationArchivedStatus( _
       ByVal _specificationName_ As String, _
       ByVal _isArchived_ As Boolean _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupSpecifications](topic3355.md)
    Dim specificationName As String
    Dim isArchived As Boolean
     
    instance.UpdateSpecificationArchivedStatus(specificationName, isArchived)  
  
C#|   
---|---  
      
    
    public void UpdateSpecificationArchivedStatus( 
       string _specificationName_ ,
       bool _isArchived_
    )  
  
#### Parameters

 _specificationName_
    The name of the specification to update.
_isArchived_
    The new value of the archived flag.

# Exceptions

Exception| Description  
---|---  
System.InvalidOperationException| The specification is running, the **DriveWorks.Specification.SpecificationContext.TryUpdateSpecificationArchivedStatus** method should be used for running specifications.  
[ItemNotFoundException](topic3571.md)| The given specification identifier is for a specification which doesn't exist.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupSpecifications Class](topic3355.md)   
[GroupSpecifications Members](topic3356.md)   
[Overload List](topic3408.md)

©2024 DriveWorks Ltd. All Rights Reserved.
