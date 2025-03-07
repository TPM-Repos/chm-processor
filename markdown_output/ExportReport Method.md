Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ExportReport Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupReports Class](topic3272.md) : ExportReport Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_reportId_
    The id of the report to export.

_path_
    

Glossary Item Box

Exports a report to the given location as a drivereport file. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function ExportReport( _
       ByVal _reportId_ As Guid, _
       ByVal _path_ As String _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupReports](topic3272.md)
    Dim reportId As Guid
    Dim path As String
    Dim value As Boolean
     
    value = instance.ExportReport(reportId, path)  
  
C#|   
---|---  
      
    
    public bool ExportReport( 
       Guid _reportId_ ,
       string _path_
    )  
  
#### Parameters

 _reportId_
    The id of the report to export.
_path_
    

#### Return Value

Success

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupReports Class](topic3272.md)   
[GroupReports Members](topic3273.md)


