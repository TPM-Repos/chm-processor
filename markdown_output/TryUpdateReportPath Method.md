       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryUpdateReportPath Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupReports Class](topic3272.md) : TryUpdateReportPath Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_id_
    The identification of the report to update.

_newPath_
    The new directory of the report.

Glossary Item Box

Attempts to update the reports directory. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TryUpdateReportPath( _
       ByVal _id_ As Guid, _
       ByVal _newPath_ As String _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupReports](topic3272.md)
    Dim id As Guid
    Dim newPath As String
    Dim value As Boolean
     
    value = instance.TryUpdateReportPath(id, newPath)  
  
C#|   
---|---  
      
    
    public bool TryUpdateReportPath( 
       Guid _id_ ,
       string _newPath_
    )  
  
#### Parameters

 _id_
    The identification of the report to update.
_newPath_
    The new directory of the report.

#### Return Value

True if the report directory is successfully updated.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupReports Class](topic3272.md)   
[GroupReports Members](topic3273.md)


