WindowsAuthentication Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [SqlServerExport Class](topic5417.md) : WindowsAuthentication Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Determines whether to use Windows Authentication to connect to the SQL Server. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property WindowsAuthentication As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SqlServerExport](topic5417.md)
    Dim value As Boolean
     
    instance.WindowsAuthentication = value
     
    value = instance.WindowsAuthentication  
  
C#|   
---|---  
      
    
    public bool WindowsAuthentication {get; set;}  
  
# Remarks

If false SQL Server Authentication is used instead.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SqlServerExport Class](topic5417.md)   
[SqlServerExport Members](topic5418.md)


