Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Clear Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [Teams Class](topic11737.md) : Clear Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Clears the list of teams allowed by this instance. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub Clear()   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Teams](topic11737.md)
     
    instance.Clear()  
  
C#|   
---|---  
      
    
    public void Clear()  
  
# Remarks

If the instance is marked as "All Teams Allowed", i.e. the [IsUniversal](topic11756.md) property returns true, then this method will set the [IsUniversal](topic11756.md) property to false.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Teams Class](topic11737.md)   
[Teams Members](topic11738.md)


