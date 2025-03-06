ReportEntries Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [IReportProcessItem Interface](topic2285.md) : ReportEntries Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

A list of all child report entries. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Property ReportEntries As List(Of IReportEntryItem)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IReportProcessItem](topic2285.md)
    Dim value As List(Of IReportEntryItem)
     
    instance.ReportEntries = value
     
    value = instance.ReportEntries  
  
C#|   
---|---  
      
    
    List<IReportEntryItem> ReportEntries {get; set;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IReportProcessItem Interface](topic2285.md)   
[IReportProcessItem Members](topic2286.md)


