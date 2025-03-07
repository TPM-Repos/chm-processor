Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Permissions Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [SqlTestResult Class](topic5450.md) : Permissions Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

A full collection of SQL permissions that were associated with the connection on the SQL server. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <DataMemberAttribute()>
    Public Property Permissions As String()  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SqlTestResult](topic5450.md)
    Dim value() As String
     
    instance.Permissions = value
     
    value = instance.Permissions  
  
C#|   
---|---  
      
    
    [DataMemberAttribute()]
    public string[] Permissions {get; set;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SqlTestResult Class](topic5450.md)   
[SqlTestResult Members](topic5451.md)


