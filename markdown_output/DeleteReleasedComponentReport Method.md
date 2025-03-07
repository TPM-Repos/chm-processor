Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DeleteReleasedComponentReport Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupReleasedComponents Class](topic3238.md) : DeleteReleasedComponentReport Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_reportId_
    The component report to delete.

Glossary Item Box

Deletes the specified component report. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function DeleteReleasedComponentReport( _
       ByVal _reportId_ As Guid _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupReleasedComponents](topic3238.md)
    Dim reportId As Guid
    Dim value As Boolean
     
    value = instance.DeleteReleasedComponentReport(reportId)  
  
C#|   
---|---  
      
    
    public bool DeleteReleasedComponentReport( 
       Guid _reportId_
    )  
  
#### Parameters

 _reportId_
    The component report to delete.

#### Return Value

True if the report was deleted successfully.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupReleasedComponents Class](topic3238.md)   
[GroupReleasedComponents Members](topic3239.md)


