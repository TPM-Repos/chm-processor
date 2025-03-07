Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DateCompleted Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ReportDetails Class](topic5221.md) : DateCompleted Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the date and time the report was completed, or a null reference if the report has not been completed. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property DateCompleted As Nullable(Of Date)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReportDetails](topic5221.md)
    Dim value As Nullable(Of Date)
     
    value = instance.DateCompleted  
  
C#|   
---|---  
      
    
    public Nullable<DateTime> DateCompleted {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReportDetails Class](topic5221.md)   
[ReportDetails Members](topic5222.md)


