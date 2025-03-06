       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
UpdateArchivedState Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic11194.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationContext Class](topic11149.md) : UpdateArchivedState Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_isArchived_
    The new value of the archived flag.

Glossary Item Box

Sets the archived state of a loaded/running specification. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub UpdateArchivedState( _
       ByVal _isArchived_ As Boolean _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationContext](topic11149.md)
    Dim isArchived As Boolean
     
    instance.UpdateArchivedState(isArchived)  
  
C#|   
---|---  
      
    
    public void UpdateArchivedState( 
       bool _isArchived_
    )  
  
#### Parameters

 _isArchived_
    The new value of the archived flag.

# Exceptions

Exception| Description  
---|---  
System.InvalidOperationException| A specification must be loaded in order to update its archived state.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationContext Class](topic11149.md)   
[SpecificationContext Members](topic11150.md)

©2024 DriveWorks Ltd. All Rights Reserved.
