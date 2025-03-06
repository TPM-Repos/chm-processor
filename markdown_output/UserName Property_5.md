       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Username Property   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic6819.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Connectors.Database Namespace](topic6754.md) > [SqlDataSourceConfiguration Class](topic6807.md) : Username Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets the username to use when connecting to the SQL server. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property Username As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SqlDataSourceConfiguration](topic6807.md)
    Dim value As String
     
    instance.Username = value
     
    value = instance.Username  
  
C#|   
---|---  
      
    
    public string Username {get; set;}  
  
# Remarks

This is not used when using [IsTrustedConnection](topic6816.md).

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SqlDataSourceConfiguration Class](topic6807.md)   
[SqlDataSourceConfiguration Members](topic6808.md)

©2024 DriveWorks Ltd. All Rights Reserved.
