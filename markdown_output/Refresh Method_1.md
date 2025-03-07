Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Refresh Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectDataTable Class](topic4282.md) : Refresh Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Refreshes the data table by asking the provider to re-retrieve the data. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Refresh() As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectDataTable](topic4282.md)
    Dim value As Boolean
     
    value = instance.Refresh()  
  
C#|   
---|---  
      
    
    public bool Refresh()  
  
#### Return Value

True if the data was successfully retrieved, otherwise false.

# Remarks

If a seriously problem occurs when retrieving the data, a provider-specific exception may be thrown.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectDataTable Class](topic4282.md)   
[ProjectDataTable Members](topic4283.md)


