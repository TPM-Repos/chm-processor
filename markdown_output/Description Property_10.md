Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Description Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [IReportProcessItem Interface](topic2285.md) : Description Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

The description of the process, excluding the clone name and timing information (use Title for full description including these). 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Property Description As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IReportProcessItem](topic2285.md)
    Dim value As String
     
    instance.Description = value
     
    value = instance.Description  
  
C#|   
---|---  
      
    
    string Description {get; set;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IReportProcessItem Interface](topic2285.md)   
[IReportProcessItem Members](topic2286.md)


