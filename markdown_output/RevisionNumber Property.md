RevisionNumber Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectSpecialVariables Class](topic4782.md) : RevisionNumber Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the revision number of the specification. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public MustOverride ReadOnly Property RevisionNumber As Integer  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectSpecialVariables](topic4782.md)
    Dim value As Integer
     
    value = instance.RevisionNumber  
  
C#|   
---|---  
      
    
    public abstract int RevisionNumber {get;}  
  
# Remarks

The revision number of a specification starts at 1 and is incremented each time the specification is edited.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectSpecialVariables Class](topic4782.md)   
[ProjectSpecialVariables Members](topic4783.md)


