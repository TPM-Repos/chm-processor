Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RefreshOnProjectLoad Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectDataTable Class](topic4282.md) : RefreshOnProjectLoad Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Determines if the data table is to be refreshed each time the project is loaded. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overridable Function RefreshOnProjectLoad() As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectDataTable](topic4282.md)
    Dim value As Boolean
     
    value = instance.RefreshOnProjectLoad()  
  
C#|   
---|---  
      
    
    protected virtual bool RefreshOnProjectLoad()  
  
#### Return Value

True if the data table is to be refreshed on project load.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectDataTable Class](topic4282.md)   
[ProjectDataTable Members](topic4283.md)


