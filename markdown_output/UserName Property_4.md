Username Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Connectors.Database Namespace](topic6754.md) > [OdbcDataSourceConfiguration Class](topic6796.md) : Username Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets user name to use to access the data source. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property Username As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [OdbcDataSourceConfiguration](topic6796.md)
    Dim value As String
     
    instance.Username = value
     
    value = instance.Username  
  
C#|   
---|---  
      
    
    public string Username {get; set;}  
  
# Remarks

This can be left blank if no login credentials are required.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[OdbcDataSourceConfiguration Class](topic6796.md)   
[OdbcDataSourceConfiguration Members](topic6797.md)


