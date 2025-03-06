WindowsAuthentication Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [SqlServerDataTable Class](topic5396.md) : WindowsAuthentication Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Whether to use Windows authentication to sign into the SQL database. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property WindowsAuthentication As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SqlServerDataTable](topic5396.md)
    Dim value As Boolean
     
    instance.WindowsAuthentication = value
     
    value = instance.WindowsAuthentication  
  
C#|   
---|---  
      
    
    public bool WindowsAuthentication {get; set;}  
  
# Remarks

Setting this value to true will clear the currently stored Username and Password.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SqlServerDataTable Class](topic5396.md)   
[SqlServerDataTable Members](topic5397.md)


