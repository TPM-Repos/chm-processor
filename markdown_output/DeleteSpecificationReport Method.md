Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DeleteSpecificationReport Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSpecifications Class](topic3355.md) : DeleteSpecificationReport Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_reportId_
    The report to delete.

Glossary Item Box

Deletes the specification report with the specified identifier. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub DeleteSpecificationReport( _
       ByVal _reportId_ As Guid _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupSpecifications](topic3355.md)
    Dim reportId As Guid
     
    instance.DeleteSpecificationReport(reportId)  
  
C#|   
---|---  
      
    
    public void DeleteSpecificationReport( 
       Guid _reportId_
    )  
  
#### Parameters

 _reportId_
    The report to delete.

# Exceptions

Exception| Description  
---|---  
[ItemNotFoundException](topic3571.md)| The report does not exist.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupSpecifications Class](topic3355.md)   
[GroupSpecifications Members](topic3356.md)


