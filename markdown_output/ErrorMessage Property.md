Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ErrorMessage Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [SqlTestResult Class](topic5450.md) : ErrorMessage Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

An error reported from attempting a connection to the SQL server (or Null if there were no issues). 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <DataMemberAttribute()>
    Public Property ErrorMessage As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SqlTestResult](topic5450.md)
    Dim value As String
     
    instance.ErrorMessage = value
     
    value = instance.ErrorMessage  
  
C#|   
---|---  
      
    
    [DataMemberAttribute()]
    public string ErrorMessage {get; set;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SqlTestResult Class](topic5450.md)   
[SqlTestResult Members](topic5451.md)


