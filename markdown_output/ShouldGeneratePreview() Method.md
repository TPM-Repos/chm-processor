ShouldGeneratePreview() Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectDocument Class](topic4356.md) > [ShouldGeneratePreview Method](topic4386.md) : ShouldGeneratePreview() Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Determines whether the document should be generated during preview. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function ShouldGeneratePreview() As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectDocument](topic4356.md)
    Dim value As Boolean
     
    value = instance.ShouldGeneratePreview()  
  
C#|   
---|---  
      
    
    public bool ShouldGeneratePreview()  
  
#### Return Value

Returns True if the document should be generated during preview.

# Remarks

Uses rules result from current project state.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectDocument Class](topic4356.md)   
[ProjectDocument Members](topic4357.md)   
[Overload List](topic4386.md)


