Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateReportWriter Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupReleasedComponents Class](topic3238.md) : CreateReportWriter Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_componentId_
    The identifier of the component for which to write the report.

_title_
    The title of the report.

_level_
    The maximum entry level to write to the report.

Glossary Item Box

Creates a new report writer which will write a report for the given component. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateReportWriter( _
       ByVal _componentId_ As Guid, _
       ByVal _title_ As String, _
       ByVal _level_ As [ReportingLevel](topic10362.md) _
    ) As [IGroupReportWriter](topic2207.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupReleasedComponents](topic3238.md)
    Dim componentId As Guid
    Dim title As String
    Dim level As [ReportingLevel](topic10362.md)
    Dim value As [IGroupReportWriter](topic2207.md)
     
    value = instance.CreateReportWriter(componentId, title, level)  
  
C#|   
---|---  
      
    
    public [IGroupReportWriter](topic2207.md) CreateReportWriter( 
       Guid _componentId_ ,
       string _title_ ,
       [ReportingLevel](topic10362.md) _level_
    )  
  
#### Parameters

 _componentId_
    The identifier of the component for which to write the report.
_title_
    The title of the report.
_level_
    The maximum entry level to write to the report.

#### Return Value

A report writer.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupReleasedComponents Class](topic3238.md)   
[GroupReleasedComponents Members](topic3239.md)


