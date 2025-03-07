Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateReportWriter Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Reporting Namespace](topic10334.md) > [ReportPackage Class](topic10451.md) : CreateReportWriter Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_title_
    The title of the report to create.

Glossary Item Box

Creates a new report with the given title in the package. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateReportWriter( _
       ByVal _title_ As String _
    ) As [IReportWriter](topic10344.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReportPackage](topic10451.md)
    Dim title As String
    Dim value As [IReportWriter](topic10344.md)
     
    value = instance.CreateReportWriter(title)  
  
C#|   
---|---  
      
    
    public [IReportWriter](topic10344.md) CreateReportWriter( 
       string _title_
    )  
  
#### Parameters

 _title_
    The title of the report to create.

#### Return Value

A report writer for the given report.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReportPackage Class](topic10451.md)   
[ReportPackage Members](topic10452.md)


