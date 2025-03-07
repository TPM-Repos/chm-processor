Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IApplicationModule Interface   
[Members](topic1998.md)   
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Extensibility Namespace](topic1995.md) : IApplicationModule Interface  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Provides a contract for a module of a DriveWorks application. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <EditorBrowsableAttribute(EditorBrowsableState.Advanced)>
    Public Interface IApplicationModule 
       Inherits [DriveWorks.Extensibility.IExtension](topic7152.md)   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IApplicationModule](topic1997.md)  
  
C#|   
---|---  
      
    
    [EditorBrowsableAttribute(EditorBrowsableState.Advanced)]
    public interface IApplicationModule : [DriveWorks.Extensibility.IExtension](topic7152.md)    
  
# Remarks

Modules provide the same capabilities as plugins but are not shown in an applications plugin configuration UI and do not expose any configurability. Unless there is a very specific reason why these two conditions should be true, you should consider using the [IApplicationPlugin](topic2004.md) interface to extend a DriveWorks application instead.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IApplicationModule Members](topic1998.md)   
[DriveWorks.Applications.Extensibility Namespace](topic1995.md)


