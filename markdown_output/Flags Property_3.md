Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Flags Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [ReleaseEnvironment Class](topic6379.md) : Flags Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets the flags to apply to the released components. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property Flags As [ReleasedComponentFlags](topic6145.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleaseEnvironment](topic6379.md)
    Dim value As [ReleasedComponentFlags](topic6145.md)
     
    instance.Flags = value
     
    value = instance.Flags  
  
C#|   
---|---  
      
    
    public [ReleasedComponentFlags](topic6145.md) Flags {get; set;}  
  
# Remarks

The default is [ReleasedComponentFlags.None](topic6145.md).

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleaseEnvironment Class](topic6379.md)   
[ReleaseEnvironment Members](topic6380.md)


