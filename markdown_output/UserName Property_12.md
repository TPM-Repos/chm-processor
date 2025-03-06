UserName Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [SqlServerExport Class](topic5417.md) : UserName Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/Sets the Username that is used to connect to the SQL Server. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property UserName As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SqlServerExport](topic5417.md)
    Dim value As String
     
    instance.UserName = value
     
    value = instance.UserName  
  
C#|   
---|---  
      
    
    public string UserName {get; set;}  
  
# Remarks

May be nothing if Windows Authentication is used to connect to the SQL Server.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SqlServerExport Class](topic5417.md)   
[SqlServerExport Members](topic5418.md)


