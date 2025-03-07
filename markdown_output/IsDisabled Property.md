Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IsDisabled Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ConnectionManager Class](topic2554.md) : IsDisabled Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets or sets whether database connections are currently disabled. Note, changing the disabled state will not cause rules to be recalculated. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property IsDisabled As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ConnectionManager](topic2554.md)
    Dim value As Boolean
     
    instance.IsDisabled = value
     
    value = instance.IsDisabled  
  
C#|   
---|---  
      
    
    public bool IsDisabled {get; set;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ConnectionManager Class](topic2554.md)   
[ConnectionManager Members](topic2555.md)


