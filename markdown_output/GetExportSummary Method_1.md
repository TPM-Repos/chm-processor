Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetExportSummary Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [IDataExportDefinition Interface](topic2177.md) : GetExportSummary Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Determines what would happen per-row if the export were executed. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function GetExportSummary() As [DataExportSummaryInfo()](topic2644.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IDataExportDefinition](topic2177.md)
    Dim value() As [DataExportSummaryInfo](topic2644.md)
     
    value = instance.GetExportSummary()  
  
C#|   
---|---  
      
    
    [DataExportSummaryInfo[]](topic2644.md) GetExportSummary()  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IDataExportDefinition Interface](topic2177.md)   
[IDataExportDefinition Members](topic2178.md)


