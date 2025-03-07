Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetConnectionString Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupConnectionStringBuilder Class](topic3068.md) : GetConnectionString Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets a group connection string based on the current property values. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetConnectionString() As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupConnectionStringBuilder](topic3068.md)
    Dim value As String
     
    value = instance.GetConnectionString()  
  
C#|   
---|---  
      
    
    public string GetConnectionString()  
  
# Exceptions

Exception| Description  
---|---  
System.InvalidOperationException| Throw when there are invalid values in properties.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupConnectionStringBuilder Class](topic3068.md)   
[GroupConnectionStringBuilder Members](topic3069.md)


