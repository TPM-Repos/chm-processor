       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryDeleteSpecificationReport Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSpecifications Class](topic3355.md) : TryDeleteSpecificationReport Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_reportId_
    The report to delete.

Glossary Item Box

Tries to delete a specification report. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TryDeleteSpecificationReport( _
       ByVal _reportId_ As Guid _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupSpecifications](topic3355.md)
    Dim reportId As Guid
    Dim value As Boolean
     
    value = instance.TryDeleteSpecificationReport(reportId)  
  
C#|   
---|---  
      
    
    public bool TryDeleteSpecificationReport( 
       Guid _reportId_
    )  
  
#### Parameters

 _reportId_
    The report to delete.

#### Return Value

True if the report was found and deleted, false if it didn't exist.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupSpecifications Class](topic3355.md)   
[GroupSpecifications Members](topic3356.md)


