Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Password Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [SqlServerExport Class](topic5417.md) : Password Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/Sets the Password that is used to connect to the SQL Server. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property Password As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SqlServerExport](topic5417.md)
    Dim value As String
     
    instance.Password = value
     
    value = instance.Password  
  
C#|   
---|---  
      
    
    public string Password {get; set;}  
  
# Remarks

May be nothing if Windows Authentication is used to connect to the SQL Server.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SqlServerExport Class](topic5417.md)   
[SqlServerExport Members](topic5418.md)


